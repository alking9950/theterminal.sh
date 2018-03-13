The following files were generated on March 12 by obtaining the output of the
following urls:


* restricted: http://theterminal.sh/mem/write?bus=keys&i=caller
* convert: http://theterminal.sh/mem/write?bus=16&i[toString]=1
  (thanks yeniborsa]


The way this worked (bug has been fixed) is that the memory is in a nested array of the syntax:


    data = [ [...], [...], ... ]

Where each inner array has 32 items, and there are 17 such arrays in the outter
array. The program is accessing items in the array like so:

    data[BUS][i]

Originally there were boundary checks so any out-of-bound numbers would result
in an immediate return of `-1`, but there was no such checking if the result
was a string. Hence the error dumps that occurred.