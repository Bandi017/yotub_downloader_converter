from pytube import Search

yt_vid_title = 'python for beginners'
s = Search(yt_vid_title)

for vid in s.results:
    print(vid.video_id)

# for video in s.completion_suggestions:
#     print(video)
