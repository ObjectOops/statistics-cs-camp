# Run in directory with videos.
cp ../../../../videos.txt .
ffmpeg -f concat -safe 0 -i videos.txt -c copy presentation.mp4
rm videos.txt
