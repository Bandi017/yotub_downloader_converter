from pytube import Search

yt_vid_title = 'how to use a rotary encoder'
s = Search(yt_vid_title)

for vid in s.results:
    print(vid.video_id)

for video in s.completion_suggestions:
    print(video)
