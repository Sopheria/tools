# simple script that reads a file containing a set of points and determines how tiles at those points would be sorted into a 2D spatial hash.
# The file it reads from is tiles.txt, and must contain a set of newline-delimited 2D points in (x,y) format. The output is written to tile_hash.txt.
# This file will be overwritten on each run.

def addToListIgnoringDuplicates(item, list):
	if item not in list:
		list.append(item)

def addToHistogram(key, histogram):
	if key not in histogram:
		histogram[key] = 1
	else:
		histogram[key] += 1


readfile = open("tiles.txt", "r")
writefile = open("tile_hash.txt", "w")

tilewidth = 32
tileheight = 32

mapwidth = 3200
mapheight = 3200

numhashcols = 8
numhashrows = 8

bucketwidth = mapwidth/numhashcols
bucketheight = mapheight/numhashrows

histogram = {}

for line in readfile:
	point = eval(line)
	
	hashBuckets = []

	hashId = ((point[0]*tilewidth)/bucketwidth) + numhashcols*((point[1]*tileheight)/bucketheight)
	x = (point[0]*tilewidth)/bucketwidth
	y = (point[1]*tileheight)/bucketheight
	yfinal = numhashcols*y

	addToListIgnoringDuplicates(hashId, hashBuckets)

	hashId = ((point[0]*tilewidth + tilewidth)/bucketwidth) + numhashcols*((point[1]*tileheight)/bucketheight)
	addToListIgnoringDuplicates(hashId, hashBuckets)
	x = (point[0]*tilewidth + tilewidth)/bucketwidth
	y = (point[1]*tileheight)/bucketheight
	yfinal = numhashcols*y

	hashId = ((point[0]*tilewidth + tilewidth)/bucketwidth) + numhashcols*((point[1]*tileheight + tileheight)/bucketheight)
	addToListIgnoringDuplicates(hashId, hashBuckets)
	x = (point[0]*tilewidth + tilewidth)/bucketwidth
	y = (point[1]*tileheight + tileheight)/bucketheight
	yfinal = numhashcols*y

	hashId = ((point[0]*tilewidth)/bucketwidth) + numhashcols*((point[1]*tileheight + tileheight)/bucketheight)
	addToListIgnoringDuplicates(hashId, hashBuckets)
	x = (point[0]*tilewidth)/bucketwidth
	y = (point[1]*tileheight + tileheight)/bucketheight
	yfinal = numhashcols*y

	for bucket in hashBuckets:
		addToHistogram(bucket, histogram)

	writefile.write(str(point))

	writefile.write(" -> ");

	writefile.write(str(hashBuckets))
	writefile.write("\n")

writefile.write("\n")

for key in histogram:
	writefile.write(str(key))
	writefile.write(":\t")
	writefile.write(str(histogram[key]))
	writefile.write("\n")

readfile.close()
writefile.close()
