# Game of Bottles HackBulgaria problem
class Bottle
  attr_accessor :x, :y
  def initialize(x, y)
    @x = x
    @y = y
  end

  def to_s
    @x + ' ' + @y
  end

  def find_distance(other)
    ((@x.to_i - other.x.to_i) + (@y.to_i - other.y.to_i)).abs
  end

  def self.game_of_bottles(bottles)
    bottles = bottles.permutation.to_a
    res = []
    bottles.each do |i|
      dist = 0
      i.each_cons(2) { |j, k| dist += k.find_distance(j) }
      res << dist
    end
    res.min
  end
end

bottles = []

n = gets.chomp.to_i
0.upto(n - 1) do |x, y|
  x, y = gets.split.map(&:to_i)
  bottles << Bottle.new(x, y)
end

puts Bottle.game_of_bottles(bottles)
