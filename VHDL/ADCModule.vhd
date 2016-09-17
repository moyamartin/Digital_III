LIBRARY ieee;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_arith.all;
USE ieee.std_logic_unsigned.all;
USE ieee.numeric_std.all;

-- *************************** REVISAR ******************************************
-- Para la sincronización con el MCP3204 se deberá tener en cuenta D_Width (18/19)
-- para los dos modos posibles o modificar cpol y cpha.

ENTITY ADC_Module IS
  GENERIC(
	 D_Width   : INTEGER  := 19;                               --Ancho de datos
	 clk_div   : INTEGER  := 25);                              --clocks del sistema por 1/2 periodo of sclk (antiguo clk ratio)
  PORT(
   clk_adc    : IN     STD_LOGIC;                             --clock del sistema	
   reset_adc  : IN     STD_LOGIC;                             --reset_adc asincrnico
   start_adc  : IN     STD_LOGIC;                             --initiate transaction
   miso_adc   : IN     STD_LOGIC;                             --master in, slave out
	sclk_adc   : BUFFER STD_LOGIC;                             --spi clock
   cs_adc : BUFFER STD_LOGIC;                             --slave select
	mosi_adc   : OUT    STD_LOGIC;                             --master out, slave in
   VData_adc  : BUFFER STD_LOGIC;                             --datos validos en la salida
	Data_adc : OUT    STD_LOGIC_VECTOR(7 DOWNTO 0)
	 );        --Salida de datos
END ADC_Module;

ARCHITECTURE logic OF ADC_Module IS
  TYPE machine IS (ready,execute);                           --Maquina de estados 
  SIGNAL state       : machine;                               --estado actual
  SIGNAL count       : INTEGER;                              --counter to trigger sclk from system clock
  SIGNAL clk_toggles : INTEGER RANGE 0 TO D_Width*2 + 1;         --count spi clock toggles
  SIGNAL assert_data : STD_LOGIC;                            --'1' is tx sclk toggle, '0' is rx sclk toggle
  SIGNAL rx_buffer   : STD_LOGIC_VECTOR(D_Width-1 DOWNTO 0);      --receive data buffer  
  SIGNAL tx_buffer   : STD_LOGIC_VECTOR(D_Width-1 DOWNTO 0);      --Bits de configuracin a transmitir
  SIGNAL last_bit_rx : INTEGER RANGE 0 TO D_Width*2 + 1;--last rx data bit location 
  SIGNAL cpol : STD_LOGIC := '0';
  SIGNAL cpha : STD_LOGIC := '0';
  SIGNAL start_jk : STD_LOGIC;
  SIGNAL temp_actual: INTEGER;
  SIGNAL temp_anterior: INTEGER;
  SIGNAL first_value: STD_LOGIC := '0';
  SIGNAL bus_counter : INTEGER RANGE 0 TO 3;
  SIGNAL valid_data : STD_LOGIC;
  SIGNAL write_signal : STD_LOGIC;
BEGIN

-- Registro JK para mantener un modo continuo del sistema
--PROCESS(clk_adc, Start, reset_adc)
--BEGIN
	--IF (reset_adc = '1') THEN
		--start_jk <= '0';
	--ELSIF(clk_adc'EVENT AND clk_adc = '1' AND Start = '1') THEN
		--start_jk <= '1';
	--END IF;
--END PROCESS;

PROCESS(clk_adc, reset_adc)
BEGIN  
	IF(reset_adc	= '1') THEN				-- reset_adc asincrónico
		VData_adc <= '0';        			-- bajar la señal de datos válidos
      cs_adc <= '1';                     	-- subir cs_adc 
      mosi_adc <= 'Z';                  	-- set master out to high impedance
		state <= ready;                	-- Al reset_adcear debe estar preparado para recibir datos
		bus_counter <= 0;
		Data_adc <= (others => 'Z');
	 ELSIF(clk_adc'EVENT AND clk_adc = '1') THEN
      CASE state IS						-- Máquina de estados
        WHEN ready =>
			 bus_counter <= 0;
			 Data_adc <= (others => 'Z');
          VData_adc <= '0';             	-- datos validos   (REVISAR) aca habia un busy que daba la informacion de estar listo
          cs_adc <= '1';                	-- mantener en alto cs_adc
          mosi_adc <= 'Z';              	-- setea mosi_adc en alta impedancia
          tx_buffer <= "1100000000000000000";
	
          -- Inicializa la transacción
          IF(start_adc = '1') THEN      	-- (REVISAR YA QUE LA IDEA DEL SETEO NO ES LA MISMA QUE PLANTEAMOS PARA EL ADC)
            VData_adc <= '0';           	-- la salida de datos no es valida
            count <= clk_div;       	-- Inicia el clock divider
			   -- Seteamos la polaridad del clock y la fase en 0
				sclk_adc <= cpol;            	
            assert_data <= NOT cpha; 	
				clk_toggles <= 0;        	-- inicial el contador del toggle (conmutador)
				last_bit_rx <= D_Width*2 + conv_integer(cpha) - 1; --set last rx data bit 
				state <= execute;        	-- Procede la ejecución de la lectura
			 ELSE
				state <= ready;          	-- mantiene el estado de preparado
			 END IF;
             
		-- Comienza la ejecución             
        WHEN execute =>
          VData_adc <= '0';        -- Mientras se ejecuta la salida de datos no es valida
          cs_adc <='0';            -- Activo chip select
          --system clock to sclk ratio is met
          IF(count = clk_div) THEN        
            count <= 1;                     --reset_adc system-to-spi clock counter
            assert_data <= NOT assert_data; --switch transmit/receive indicator
            clk_toggles <= clk_toggles + 1; --increment spi clock toggles counter
            IF(clk_toggles <= D_Width*2 AND cs_adc = '0') THEN  
              sclk_adc <= NOT sclk_adc; --toggle spi clock
            END IF;
            --receive spi clock toggle
            IF(assert_data = '0' AND clk_toggles < last_bit_rx + 1 AND cs_adc = '0') THEN 
				  -- Hace un shift de la entrada por miso (Master IN Slave OUTPUT)
              rx_buffer <= rx_buffer(D_Width-2 DOWNTO 0) & miso_adc; 
				END IF;
            
            --transmit spi clock toggle
				-- Hace un shift out de los datos de configuracion
				IF(assert_data = '1' AND clk_toggles < last_bit_rx) THEN 
					mosi_adc <= tx_buffer(D_Width-1);                     
					tx_buffer <= tx_buffer(D_Width-2 DOWNTO 0) & '0'; 
				END IF;
          
            --end of transaction
				IF(clk_toggles = D_Width*2+1) THEN     --***(de la expresion del if ha sido removido "AND cont= '0'")
					VData_adc <= '1';             --datos validos
					cs_adc <=  '1';              --poner en alto cs_adc
					mosi_adc <= 'Z';             --set mosi_adc output high impedance
					-- FILTRO PASA-BAJO.
					-- Si la diferencia entre mediciones es de un grado o mayor, toma el valor anterior
					-- NOTA: las mediciones se realizan muy rápido respecto a la velocidad del sistema
					while VData_adc = '1' loop
						if(bus_counter = 0) then
							Data_adc <= "01010100";
							bus_counter <= bus_counter + 1;
						elsif (bus_counter = 1) then
							Data_adc <= "0000" & rx_buffer(11 downto 8);
							bus_counter <= bus_counter + 1;
						elsif (bus_counter = 2) then
							Data_adc <= rx_buffer(7 downto 0);
							bus_counter <= bus_counter + 1;
						elsif (bus_counter = 3) then
							bus_counter <= 0;
							VData_adc <= '0';
							state <= ready;          --return to ready state
						end if;
					end loop;
				ELSE  
					--not end of transaction
					state <= execute;        --remain in execute state
				END IF;
			ELSE			  --system clock to sclk ratio not met
            count <= count + 1; --increment counter
            state <= execute;   --remain in execute state
         END IF;
      END CASE;
    END IF;
  END PROCESS;


END logic;