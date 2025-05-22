# image-grab
Two scripts I've used to grab .png and .jpg files from archives, binaries, and other types of files. For effectiveness, I fixed up my code so that it can take a filename as an argument instead of having to manually edit in what file you want the script to work with.

I've used these scripts to extract files from old Android games before.

You are generally free to take the code and put in the magic number of some other file format, or even fork this repo and add case handling (which I'm too lazy to add).

These scripts are functionally similar to this [BMS script](https://github.com/calmevening/evangelion-android-quickbms-script/) I asked for back in 2023.

## Usage
``python png.py filename.extension``<br/>
``python jpg.py filename.extension``<br/>
``python bmp.py filename.extension``

Note: python is important as the script breaks without it

## Effectivity
The png script is guaranteed to always work.

The jpg script is hit or miss as it does not have case handling, and thus only targets the first three hex chars of .jpg's magic numbers (``FF D8 FF``). This means that using this script may generate a lot of false positive .jpg files. Might add case handling in the future so it can target multiple different types of .jpg files.

The bmp script has only ever been used on binary files from 1990s-2000s era software. Since the magic number of bitmaps (``42 4D``) is too short and too common, I recommend only using these if you know for certain the thing you're trying to extract uses .bmp files, otherwise the script might generate a lot of false positive files.

bmp_corrected.py is an alternate version of the bmp script that has increased effectivity from the original bmp script, at the cost that it might not be able to target all types of bmp files. It checks between four magic numbers instead of just one, and this can be expanded.
