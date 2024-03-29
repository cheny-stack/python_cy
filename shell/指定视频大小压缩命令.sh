
input_file="1280.mp4"

currentTime=`date "+%Y-%m-%d%H%M%S"`
file="ffmpeg_$currentTime.mp4"
echo $file
ffmpeg -i "$input_file" -s 960*540 "$file"

# 25MB target size
target_size_mb=2
# target size in bits
target_size=$(( $target_size_mb * 1000 * 1000 * 8 ))
length=`ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$file"`
length_round_up=$(( ${length%.*} + 1 ))
total_bitrate=$(( $target_size / $length_round_up ))
# 128k bit rate
audio_bitrate=$(( 32 * 1000 )) 
video_bitrate=$(( $total_bitrate - $audio_bitrate ))
ffmpeg -i "$file" -b:v $video_bitrate -maxrate:v $video_bitrate -bufsize:v $(( $target_size / 20 )) -b:a $audio_bitrate "${file}-${target_size_mb}mb.mp4"
rm -f $file