imagen=imread('planeta_8k.jpg');
J = imnoise(imagen,'salt & pepper');
imshow(J)
