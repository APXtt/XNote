import os, youtube_dl, urllib.request

# youtube_download_url : 다운로드 하는 유튜브 url
# download_folder : 다운로드하는 폴더
# youtube_download : 다운받을 경로와 다운받을 url을 입력하면 다운로드가 됨

youtube_url = 'https://www.youtube.com/watch?v=sTnShKZmhFo'
download_folder = 'C:\\Users\\gbytt\\Downloads\\'

def youtube_download(output_dir, youtube_download_url):
    download_path = os.path.join(output_dir, '%(title)s.%(ext)s')

    ydl_opts = {
        'format' : 'best/best',
        'outtmpl' : download_path,
        'writesubtitles' : False,
        'writethumbnail' : False,
        'writeautomaticsub' : False,
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_download_url])
    except Exception as e:
        print('error', e)

youtube_download(download_folder, youtube_url)