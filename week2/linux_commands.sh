mkdir -p A/C/F/G
mkdir -p A/B
mkdir -p A/C/E
mkdir -p A/D/H
mkdir -p A/D/I

echo "A Panda bear walks into a restaurant. He orders a meal and eats it.
After politely paying for his meal, he pulls out a gun and shoots it in the air. He immediately walks out the door. \"Why did you do that?\" hollered the confused waitress.
Looking back over his shoulder the panda says \"I'm a panda\". \"Look it up in the dictionary.\"
The waitress locates the dictionary on her bosses desk and searches for the definition of panda bear.
Finding it she reads, \"Panda Bear - A large black and white bear like mammal native to the far east.
Eats shoots and leaves." > A/C/F/G/panda

cp A/C/F/G/panda A/C/F/G/panda1 & cp A/C/F/G/panda A/C/F/G/panda2 & cp A/C/F/G/panda A/C/F/G/panda3 & rm A/C/F/G/panda

touch A/C/F/G/penguin1 & touch A/C/F/G/penguin2 & touch A/C/F/G/penguin3

cp -R A/C/F/G A/C/E/J 