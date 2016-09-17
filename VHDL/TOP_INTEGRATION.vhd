----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    13:03:17 05/13/2016 
-- Design Name: 
-- Module Name:    TOP_INTEGRATION - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity TOP_INTEGRATION is
	port(
		rx_sys : in std_logic;
		tx_sys : out std_logic;
		clk_sys : in std_logic;
		reset_sys : in std_logic;
		miso_sys: in std_logic;
		mosi_sys : out std_logic;
		cs_sys : out std_logic;
		sclk_sys : out std_logic;
		start_sys : in std_logic;
		led_sys: out std_logig
	);
end TOP_INTEGRATION;

architecture Behavioral of TOP_INTEGRATION is

component timer10ms is
	port( 
		clk, reset: in std_logic;
		tick: out std_logic
		);
end component;

component Top_UART is 
	generic(
			DBIT: integer := 8;
			SB_TICK: integer := 16;
			N: integer := 5;
			M: integer := 27
			);
			
	port( rx_uart: in std_logic;
			tx_uart: out std_logic;
			clk_uart: in std_logic;
			reset_uart: in std_logic;
			rd_uart, wr_uart: in std_logic;
			rx_full_uart: out std_logic;
			r_data_uart: out std_logic_vector(DBIT-1 downto 0);
			w_data_uart: in std_logic_vector(DBIT-1 downto 0)
			);
end component;

component ADC_Module is
PORT(
   clk_adc   : IN     STD_LOGIC;                             --clock del sistema	
   reset_adc  : IN     STD_LOGIC;                             --reset_adc asincrnico
   start_adc  : IN     STD_LOGIC;                             --initiate transaction
   miso_adc   : IN     STD_LOGIC;                             --master in, slave out
	sclk_adc   : BUFFER STD_LOGIC;                             --spi clock
   cs_adc 	  : BUFFER STD_LOGIC;                             --slave select
	mosi_adc   : OUT    STD_LOGIC;                             --master out, slave in
   VData_adc  : BUFFER STD_LOGIC;                             --datos validos en la salida
	Data_adc   : OUT    STD_LOGIC_VECTOR(7 DOWNTO 0)
	 );
end component; 


signal internal_clk : std_logic;
signal internal_rst : std_logic;
signal internal_data : std_logic_vector (7 downto 0);
signal internal_vdata : std_logic;
signal internal_cs : std_logic;
signal internal_sclk : std_logic;
signal internal_tick : std_logic;
signal internal_miso, internal_mosi: std_logic;

begin

internal_clk <= clk_sys;
internal_rst <= reset_sys;--not(reset_sys);
--cs_sys <= internal_cs;
--sclk_sys <= internal_sclk;
--mosi_sys <= internal_mosi;
--internal_miso <= miso_sys;

U1: ADC_Module
port map(
	clk_adc => internal_clk,
	reset_adc => internal_rst,
	start_adc => internal_tick,
	miso_adc => internal_miso,
	mosi_adc => internal_mosi,
	cs_adc => internal_cs,
	VData_adc => internal_vdata,
	Data_adc => internal_data,
	sclk_adc => internal_sclk
);

U2: Top_UART
port map(
	rx_uart => rx_sys,
	tx_uart => tx_sys,
	clk_uart => internal_clk,
	reset_uart => internal_rst,
	wr_uart => internal_vdata,
	rd_uart => 'Z',
	r_data_uart => open,
	w_data_uart => internal_data
);

U3: timer10ms
port map(
	clk => internal_clk,
	reset => internal_rst,
	tick => internal_tick
);

U4: MCP3204_SIM
port map(
	sclk_mcp =>	internal_sclk,
	reset_n_mcp => internal_rst,
	cs_mcp => internal_cs,
	mosi_mcp => internal_mosi,
	miso_mcp => internal_miso
);

end Behavioral;

