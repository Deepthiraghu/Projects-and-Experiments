
# Horizon finding
This project is to identify horizons in images. We'll assume relatively clean images, where the mountain is plainly visible, there are no other objects obstructing the mountain's ridge-line, the mountain takes up the full horizontal dimension of the image, and the sky is relatively clear. Under these assumptions, for each column of the image we need to estimate the row of the image corresponding to the boundary position. Plotting this estimated row for each column will give a horizon estimate.

The horizon finding problem is split into three parts:
## Part 1 
This is a simple approach to estimate the following:

<b>s<sub>i</sub><sup>*</sup> = arg max s<sub>i</sub> P(S<sub>i</sub>=s<sub>i</sub>|w<sub>1</sub>,..,w<sub>m</sub>)</b>

i.e, for each column in the grey-scale image, the corresponding row which has the maximum pixel value (since the color white has maximum pixel value). 

This gives us a list of row indices in the image with an assumption that the point in each column which has maximum pixel value will lie on the ridge line. However, while drawing a line using the row values estimated using this method, it is observed that the image might also have points which are not the horizon, but have a higher pixel value (like a person wearing a white shirt, or white buildings and walls). In this case, this method results in a scattered estimate, which includes many outliers scattered randomly away from the horizon boundary line (refer images below).

| ![](https://lh3.googleusercontent.com/5eSuF5XiO7zE91SZTx4bn03Hl9EqRzO_Zbo_GAQvQSYlWjqxKJza5AQRSIb71R427aYSJ1k9_PIgWg)| ![](https://lh3.googleusercontent.com/sDgK-EXaU0ZuTWx-wlfyyPmmTaXTs_S9Rt8gz4Y0h4O86ornj3mZe08qEvrM5qIqfclSfJKLyz0dzA)
|:---:|:---:|

## Part 2 
This approach involves using Viterbi algorithm to estimate the following maximum a posteriori path:

<b>arg max s<sub>1</sub>,..,s<sub>m</sub> P(S<sub>1</sub>=s<sub>1</sub>,..,S<sub>m</sub>=s<sub>m</sub>|w<sub>1</sub>,..,w<sub>m</sub>)</b>

The difference between 2.1 and 2.2 is that instead of finding the maximum pixel in each column, we use Viterbi algorithm to find the most probable sequence of row values. 
We define the following for our Viterbi algorithm:
* <b>States:</b> All possible row indices in the image (i.e, 0 to n)
* <b>Observed variables:</b> Row indices corresponding to the maximum pixel value in each column 
* <b>Initial probability:</b> 1
* <b> Emission probability:</b> Since we need an emission probability such that it is high near a strong edge and low otherwise, this is given by the grey-scale image itself. We normalize the grey-scale image (which essentially has values between 0 and 255) to have values between 0 and 1, and use this as our emission probability. 
* <b>Transition probability:</b> This is defined in a way to establish smoothness when the line is drawn from one row to another across the columns in the image. For a transition between two row whose indices have a difference of 20 or below, we assign a probability of 1 and for a difference greater than 20, we assign a transition probability of 0.  

After applying Viterbi algorithm on the image, it is observed that the most probable boundary line is found if there is a clear distinction between the sky, mountain and the rest of the image. However, if there is a large variation in intensity values (i.e, more of white in the image), this method does not find the perfect boundary line (refer images below). Another observation is that the most outliers, whose nearby values have been found to lie on the ridge line, have been eliminated by Viterbi algorithm since it is driven by the emission and transition probabilities (it estimates current row values based on previously estimated row values) . The outliers that exist after applying Viterbi algorithm are observed to occur in a sequence of columns in a particular area of the image where there is a spike in pixel intensity. This has been rectified by making use of the human input in Part 2.3

| ![](https://lh3.googleusercontent.com/EtuAZlAdwM2Op0SM1HiSX0E30tLy9XY8TSIC35U1di7e1sODpSF5UsbKx6N6gcn8ZWKUJhR6LfRN0A)| ![](https://lh3.googleusercontent.com/WqhGap2X-3mmVnZnTIOwqJxZv4ZFTpOTzVHQhyzBFsI_Ov_FlXRWnQE3QrrB68eNUS-S04OckWxMdw)
|:---:|:---:|


## Part 3 

In Part 2.3, a human input is provided which is a row and column corresponding to a point that lies on the horizon line. Using this new information, we modify our probabilities to help the Viterbi algorithm make a better estimate on the horizon line. 
We define the following for our Viterbi algorithm:
* <b>States:</b> Same as in Part 2.2 
* <b>Observed variables:</b> Same as in Part 2.2 
* <b>New Initial probability:</b> The pixel value corresponding to the row and column value given by human, normalized between 0 and 1
* <b>New Emission probability:</b> Since we need an emission probability such that it is high near a strong edge and low otherwise, this is given by the grey-scale image itself. We normalize the grey-scale image (which essentially has values between 0 and 255) to have values between 0 and 1, and use this as our emission probability. Additionally, based on the pixel value given by human, we assume that all rows below the human provided row value + 10 can be ignored. For example, if the human gives 20 as input, we ignore all rows below 30. This assumption is made based on another assumption that the human looks at the image and gives the lowest point on the horizon line. Since we are looking at estimating a horizon boundary between mountain and sky, it is assumed that the boundary line cannot go below the lowest point of the mountain. To incorporate this assumption, we make the emission probabilities of all the cells below the human provided row + 10 as 0. We also make the emission probability of human provided pixel as 1, since we know this point definitely lies on the horizon line.

* <b>Transition probability:</b> Same as in Part 2.2

After incorporating these changes, it is observed that the algorithm estimates a better horizon boundary line, when compared to Part 2.3 (refer image below).

| ![](https://lh3.googleusercontent.com/ZmhgWz0IzHgJ0lMzuiyHPXAlbn4qWDtenNTII98j_fHJ2glMBSEFC0SXI51AEs5JR54xaWxKWfz1dg)| ![](https://lh3.googleusercontent.com/k6yT-UKte28mnsJQ75kvbUychPnOjxzjhV-nHCbp-XjbCMBquy4pjD0qfwe9XPH36vQcuxRoXnhQDg)
|:---:|:---:|

## Illustration of improved estimate of horizon line:
Output of Part 2.1 is marked by a blue ridge line, Part 2.2 with a red line and Part 2.3 with a green line

| ![](https://lh3.googleusercontent.com/XqytJyCapBNIyJfFnXhdzaN-vPaT4uNfp3aItWgaiig8uAmt3IHCDPN0g4dvT8t_db1_DnhXuPz7sA) | ![](https://lh3.googleusercontent.com/NyQbt70ns74VLP-PBVCikHM-qzFIl6F05-CQ38W1HNM_5I8wsWL9ro1Wn7biFCH8FmQSa1paO8FoyA) | ![](https://lh3.googleusercontent.com/O4W-9fGoRmP9cd6dax15jsepcMny2N9pZfuSwlE8u13Az-N6W6vAm68_e6SAwZxvC0RWNaN8WQ8Cbg)|
|:---:|:---:|:---:|
