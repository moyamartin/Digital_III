----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    18:26:23 04/23/2016 
-- Design Name: 
-- Module Name:    timer10ms - Behavioral 
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
use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity timer10ms is

port( clk, reset: in std_logic;
		tick: out std_logic
		);
end timer10ms;

architecture Behavioral of timer10ms is
	signal r_reg: unsigned(31 downto 0);
	signal r_next: unsigned(31 downto 0);

begin
	process(clk, reset)
	begin
		if (reset = '1') then
			r_reg <= (others => '0');
		elsif (clk'event and clk='1') then
			r_reg <= r_next;
		end if;
	end process;
	
-- next state logic
r_next <= (others => '0') when r_reg=(500000) else
r_reg + 1;

-- output logic
tick <= '1' when r_reg=(500000) else '0';
end Behavioral;

