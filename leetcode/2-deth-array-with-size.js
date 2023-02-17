
array = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]


for (size=1; size<=array.length; size++) {
    for (x=0; x<=array.length-size; x++) {
        for (y=0; y<=array.length-size; y++) {
            console.log("size", size);
            for (i=x; i<x+size; i++) {
                for (j=y; j<y+size; j++) {
                    console.log(i,j);
                }
            }
        }
    }
}