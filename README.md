# K-Size sliding window to find highest sum of subsequence in array.
## Usage
Using this tool is as easy as going to your terminal and typing: 
```
python find_subsequence.py path/to/txt/file n behavior
```
Where `n` is the max length of the subsequence to search for, `path/to/txt/file` is the absolute or relative file path to the file with the space-separated integer sequence, and `behavior` refers to how you want the metric to be calculated. For example:
```
python find_subsequence.py data/input_1.txt 5 values
```
will find the maximum sum of subarrays smaller than or equal to 5 in the integer sequence, and:
```
python find_subsequence.py data/input_1.txt 5 differences
```
will find the maximum sum of possible subsequences of absolute values of the differences of neighboring pairs.

## Notes on my solution
I really tried to get the solution as O(n), however I wasn't quite able to beat O(kn).
