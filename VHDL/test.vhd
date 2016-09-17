--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   21:27:30 05/23/2016
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/Proyects/Integration/test.vhd
-- Project Name:  Integration
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: TOP_INTEGRATION
-- 
-- Dependencies:
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
--
-- Notes: 
-- This testbench has been automatically generated using types std_logic and
-- std_logic_vector for the ports of the unit under test.  Xilinx recommends
-- that these types always be used for the top-level I/O of a design in order
-- to guarantee that the testbench will bind correctly to the post-implementation 
-- simulation model.
--------------------------------------------------------------------------------
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY test IS
END test;
 
ARCHITECTURE behavior OF test IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT TOP_INTEGRATION
    PORT(
         rx_sys : IN  std_logic;
         tx_sys : OUT  std_logic;
         clk_sys : IN  std_logic;
         reset_sys : IN  std_logic
--         led_sys : OUT  std_logic
        );
    END COMPONENT;
    

   --Inputs
   signal rx_sys : std_logic := '0';
   signal clk_sys : std_logic := '0';
   signal reset_sys : std_logic := '0';

 	--Outputs
   signal tx_sys : std_logic;
   signal led_sys : std_logic;

   -- Clock period definitions
   constant clk_sys_period : time := 20 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: TOP_INTEGRATION PORT MAP (
          rx_sys => rx_sys,
          tx_sys => tx_sys,
          clk_sys => clk_sys,
          reset_sys => reset_sys
--          led_sys => led_sys
        );

   -- Clock process definitions
   clk_sys_process :process
   begin
		clk_sys <= '0';
		wait for clk_sys_period/2;
		clk_sys <= '1';
		wait for clk_sys_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
		reset_sys <= '1';
      wait for 100 ns;	

      wait for clk_sys_period*10;

      -- insert stimulus here 
		reset_sys <= '0';

      wait;
   end process;

END;
