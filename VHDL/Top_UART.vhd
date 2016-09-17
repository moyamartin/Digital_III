----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    16:41:48 03/29/2016 
-- Design Name: 
-- Module Name:    Top_UART - Behavioral 
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

entity Top_UART is
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
end Top_UART;

architecture Behavioral of Top_UART is

component uart_tx
	port(
			clk, reset: in std_logic;
			tx_start: in std_logic;
			s_tick: in std_logic;
			din: in std_logic_vector(DBIT-1 downto 0);
			tx_done_tick: out std_logic;
			tx: out std_logic
			);
end component;

Component uart_rx
	port(
			clk, reset: in std_logic;
			rx: in std_logic;
			s_tick: in std_logic;
			rx_done_tick: out std_logic;
			dout: out std_logic_vector(DBIT-1 downto 0)
			);
end component;

component mod_m_cnter
	port(
			clk, reset: in std_logic;
			max_tick: out std_logic;
			q: out std_logic_vector(N-1 downto 0)
			);
end component;

component flag_buff
	port(
		clk, reset: in std_logic;
		clr_flag, set_flag: in std_logic;
		din: in std_logic_vector(DBIT-1 downto 0);
		dout: out std_logic_vector(DBIT-1 downto 0);
		flag: out std_logic
		);
end component;

signal rx_done, tx_done, s_tick, tx_start: std_logic;
signal tx_bus, rx_bus: std_logic_vector(DBIT-1 downto 0);

begin

U1: uart_rx
port map (clk => clk_uart, 
			 reset => reset_uart,
			 rx => rx_uart, 
			 dout => rx_bus, 
			 s_tick => s_tick, --cambiar a s_tick
			 rx_done_tick => rx_done);
			 
U2: flag_buff
port map (din => rx_bus,
			 set_flag => rx_done,
			 clr_flag => rd_uart,
			 flag => rx_full_uart,
			 dout => r_data_uart,
			 clk => clk_uart,
			 reset => reset_uart);
			 
U3: uart_tx
port map (clk => clk_uart,
			 reset => reset_uart,
			 tx => tx_uart,
			 s_tick => s_tick, -- cambiar a s_tick
			 tx_start => tx_start,
			 tx_done_tick => tx_done,
			 din => tx_bus);
			 
U4: flag_buff
port map (clk => clk_uart,
			 reset => reset_uart,
			 din => w_data_uart,
			 dout => tx_bus,
			 flag => tx_start,
			 clr_flag => tx_done,
			 set_flag => wr_uart);
			 
U5: mod_m_cnter
port map (clk => clk_uart,
			 reset => reset_uart,
			 max_tick => s_tick,		--CAMBIAR a s_tick
			 q => open);
			 
end Behavioral;

