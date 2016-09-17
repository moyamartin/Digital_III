----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    16:51:54 04/23/2016 
-- Design Name: 
-- Module Name:    zztop - Behavioral 
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

entity zztop is

port( clk, rst: in std_logic;
		boton: in std_logic;
		tx: out std_logic;
		rx: in std_logic;
		led: out std_logic
		);

end zztop;

architecture Behavioral of zztop is

component Top_UART is
	generic(
			DBIT: integer := 8;
			SB_TICK: integer := 16;
			N: integer := 5;
			M: integer := 27
			);
			
	port( rx: in std_logic;
			tx: out std_logic;
			clk: in std_logic;
			reset: in std_logic;
			rd_uart, wr_uart: in std_logic;
			rx_full: out std_logic;
			r_data: out std_logic_vector(DBIT-1 downto 0);
			w_data: in std_logic_vector(DBIT-1 downto 0)
			);
	end component;

signal tx_start, enable: std_logic;
signal numero: std_logic_vector(7 downto 0);

begin



T1: Top_UART
port map(rx => rx,
			tx => tx,
			clk => clk,
			reset => not(rst),
			rd_uart => 'Z',
			wr_uart => tx_start,
			rx_full => open,
			r_data => open,
			w_data => numero
			);
			
T2: cuentaloca
port map(clk => clk,
			reset => not(rst),
			tx_start => tx_start,
			dout => numero,
			enable => enable,
			led => led);
			
T3: timer10ms
port map(clk => clk,
			reset => not(rst),
			tick => enable);
			
			

end Behavioral;

