-- Generated by Lava 2000

use work.all;

entity
  twoBitSorter
is
port
  -- clock
  ( clk : in bit

  -- inputs
  ; a : in bit
  ; b : in bit

  -- outputs
  ; smaller : out bit
  ; bigger : out bit
  );
end entity twoBitSorter;

architecture
  structural
of
  twoBitSorter
is
  signal w1 : bit;
  signal w2 : bit;
  signal w3 : bit;
  signal w4 : bit;
begin
  c_w2      : entity id    port map (clk, a, w2);
  c_w3      : entity id    port map (clk, b, w3);
  c_w1      : entity and2  port map (clk, w2, w3, w1);
  c_w4      : entity or2   port map (clk, w2, w3, w4);

  -- naming outputs
  c_smaller : entity id    port map (clk, w1, smaller);
  c_bigger  : entity id    port map (clk, w4, bigger);
end structural;
