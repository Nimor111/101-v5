def populate_hash(decode_hash, string)
  counter = 1
  0.upto(string.length) do |i|
    until string[i] != decode_hash.key(decode_hash[string[i]])
      break if i > string.length
      i += 1
    end
    (i + 1).upto(string.length) do |j|
      string[j] == string[i] ? counter += 1 : counter
    end
    decode_hash[string[i]] = counter
    counter = 1
  end
  decode_hash.delete(nil) # I really don't get this part
end

def decode(string) # string is a string aight
  decode_hash = {} # hash to hold characters and times they are repeated
  populate_hash(decode_hash, string)
  decode_hash = decode_hash.sort_by { |_, value| value }
                           .reverse.slice(0, 10).to_h
  string.split('').each do |i|
    if decode_hash.key?(string[i])
      string[i] = decode_hash.keys.reverse.index(decode_hash.key(decode_hash[
        string[i]
      ])).to_s
    end
  end
  string
end

def calculate_sum_of_numbers(string)
  result = 0
  string = string.scan(/\d+/) # isolate numbers in an array,
  # ignoring all other characters
  string.each { |i| result += i.to_i }
  result
end

puts calculate_sum_of_numbers(
  decode('bbcccddddeeeeeffffffggggggghhhhhhhhiiiiiiiiijjjjjjjjjja')
)
puts calculate_sum_of_numbers(
  decode('}w#\a:\?uxv?xvxx@axx?\u\^:a~wx?x-:u\v\a:???^xv?x??cwwx_?uhvc:w<v,:ucwzuaw::uaucwaa^ra:;?:\?xbw[^^:w::ca\wcvl\:%')
)
puts calculate_sum_of_numbers(decode('pr$pprtppp{%r%%#(;%rn$;~*s%r%r%;(#(x$p([~(~(r}%=([$[#[~[;~+rr~[r#(n([r%(n%b~;p#rp($;$[,l?(n~p#%$prn~%$r#(~$'))
puts calculate_sum_of_numbers(decode('|?=xi^.k%x||^cs^s^=||x=x|.&=..|=x=|&kv^^jkt&jzx.xx=|&&!jkjs&kj|x>j.!..^&k..&k||o&s|s=j.xx!x)j=!&s&]n|^j.!jx'))
