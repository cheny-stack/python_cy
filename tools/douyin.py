import asyncio
from douyin_tiktok_scraper.scraper import Scraper
import flask
import json
app=flask.Flask(__name__)#__name__代表当前的python文件。把当前的python文件当做一个服务启动
api = Scraper()

async def hybrid_parsing(url: str) -> dict:
    res = {}
    # Hybrid parsing(Douyin/TikTok URL)
    data = await api.hybrid_parsing(url)
    status = True if data.get('status') == 'success' else False
     # 如果解析成功
    if status:
        # 创建一个视频/图集的公有变量
        url_type = 'Video' if data.get('type') == 'video' else 'Image'
        platform = data.get('platform')
        # 如果是视频/If it's video
        if url_type == 'Video':
            res['videoURLWatermark'] = data.get('video_data').get('wm_video_url_HQ')
            res['videoURLNoWatermark'] = data.get('video_data').get('nwm_video_url_HQ')
        # 如果是图片/If it's image
        elif url_type == 'Image':
            image_list = data.get('image_data').get('no_watermark_image_list')
            res['imageList'] = image_list
    return res

@app.route('/scraper_douyin',methods=['get','post'])#第一个参数就是路径,第二个参数支持的请求方式，不写的话默认是get
def scraper_douyin():
    share_url = flask.request.json.get("share_url")
    share_test = "6.17 reo:/ 希望是最后一天感mao🤧  https://v.douyin.com/hqC9rXt/ 复制此链接，打开Dou音搜索，直接观看视频！"
    share_url = share_url if len(share_url) > 0 else share_test
    res = asyncio.run(hybrid_parsing(url= share_url))
    print("\n\n\n*********************************************************************")
    print("*********************************************************************")
    return flask.Response(json.dumps(res), mimetype='application/json')

if __name__ == "__main__":
    app.run(port=8088,debug=False,host='0.0.0.0')

    # print(scraper_douyin())
    




