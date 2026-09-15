# 配置文件，包含直播源URL、黑名单URL、公告信息、EPG URL、测速超时时间和线程池最大工作线程数

# 优先使用的IP版本，这里设置为ipv4
ip_version_priority = "ipv4"

# 直播源URL列表
source_urls = [
"https://m3u.ibert.me/fmml_ipv6.m3u",
"https://live.zbds.org/tv/iptv6.m3u",
"https://raw.githubusercontent.com/suxuang/myIPTV/refs/heads/main/ipv4.m3u",
"https://zbds.org/tv/iptv4.m3u",
"https://www.kaniptv.cc.cd",
"https://raw.githubusercontent.com/fafa002/yf2025/refs/heads/main/yiyifafa.txt",
"https://raw.githubusercontent.com/zxmlxw520/5566/refs/heads/main/cjdszb.txt",
"https://raw.githubusercontent.com/suxuang/myIPTV/main/ipv4.m3u",
"https://tv.anbox.ip-ddns.com/live",
"https://raw.githubusercontent.com/mymsnn/DailyIPTV/main/outputs/full_validated.m3u",
"https://raw.githubusercontent.com/JE668/m3u-checker-max/main/output/live.txt",
"http://wangziduoqing.com/yuan/zb.txt",
"https://raw.githubusercontent.com/807080747/zv/refs/heads/main/sese.txt",
"https://raw.githubusercontent.com/fleung49/star/refs/heads/main/mit",
"http://ge.html-5.me//ii/黄蚂蚁先锋推流源.txt",
"https://www.985pan.com/down.php/bf5e9607ff407fcdd71f63928ea5bc79.txt",
"https://raw.githubusercontent.com/alantang1977/iptv8/refs/heads/main/bbxx_lite.m3u",
"https://raw.githubusercontent.com/wujiangliu/live-sources/refs/heads/main/wangzizb.txt",
"https://raw.githubusercontent.com/wujiangliu/live-sources/refs/heads/main/shenqu.txt",
"https://gitee.com/main-stream/tv/raw/master/BOSS.json",
"https://raw.githubusercontent.com/alantang1977/iptv-auto/refs/heads/main/my.txt",
"https://raw.githubusercontent.com/ajqubbs/zhiboyuan/refs/heads/main/gatzb.txt",
"https://gitee.com/alexkw/app/raw/master/kgk.txt",

"https://live.445569.xyz/live.m3u",
"https://raw.githubusercontent.com/alantang1977/JunTV/refs/heads/main/output/result.m3u",
"https://raw.githubusercontent.com/swhtv/1/refs/heads/main/swtvlive",
"https://raw.githubusercontent.com/mhmdxahmd/mafly/refs/heads/main/MAfly1/mafly.m3u",
"http://tvv.tw/github.com/fafa002/yf2025/raw/main/yiyifafa.txt",
"https://l.gmbbk.com/upload/39183918.txt",
"https://tv123.cc.cd/tv.m3u",
"https://cdn.qd.je/live.m3u",
"https://raw.githubusercontent.com/nianxinmj/nxpz/refs/heads/main/lib/live.txt",
"https://raw.githubusercontent.com/JE668/get-m3u/main/output/source-m3u.txt",
"https://raw.githubusercontent.com/yihad168/tv/refs/heads/main/live.m3u",
"https://raw.githubusercontent.com/a2256569/tv/refs/heads/main/sdzb.txt",
"https://raw.githubusercontent.com/alantang1977/alan/main/proxy/mg.m3u",
"https://raw.githubusercontent.com/jn950/live/main/tv/pllive.txt",
"https://raw.githubusercontent.com/xJEYDAin/iptv-scraper/master/output/hk_merged.m3u",
"https://raw.githubusercontent.com/alantang1977/tvboxlive/main/tv/pllive.txt",
"https://raw.githubusercontent.com/tianze889/tvds/refs/heads/main/fyzb.txt",
"https://raw.githubusercontent.com/YueChan/Live/main/GNTV.m3u",
"https://raw.githubusercontent.com/ljlfct01/ljlfct01.github.io/refs/heads/main/zb",
"https://raw.githubusercontent.com/zilong7728/Collect-IPTV/refs/heads/main/best_sorted.m3u",
"https://raw.githubusercontent.com/BurningC4/Chinese-IPTV/master/TV-IPV4.m3u",
"https://raw.githubusercontent.com/iptv-org/iptv/gh-pages/countries/cn.m3u",
"https://raw.githubusercontent.com/iptv-org/iptv/master/streams/cn.m3u",
"https://raw.githubusercontent.com/develop202/migu_video/refs/heads/main/interface.txt",
"https://raw.githubusercontent.com/Supprise0901/TVBox_live/main/live.txt",
"https://raw.githubusercontent.com/mhmdxahmd/mafly/refs/heads/main/MAfly1/mafly.m3u",
"https://raw.githubusercontent.com/suxuang/myIPTV/main/ipv4.m3u",
"https://raw.githubusercontent.com/kimwang1978/collect-tv-txt/main/others_output.txt",
"https://raw.githubusercontent.com/alantang1977/iptv8/refs/heads/main/bbxx_lite.m3u",
"http://1.94.31.214/live/live9/dgtv.txt",
"http://1.94.31.214/live/livelite.txt",
"http://210.245.166.84:1299/live/live1.txt",
"http://210.245.166.84:1299/live/live.txt",
"https://raw.githubusercontent.com/vbskycn/iptv/master/tv/iptv4.txt",
"https://raw.githubusercontent.com/TianmuTNT/iptv/main/iptv.txt",
"https://raw.githubusercontent.com/aiyakuaile/easy_tv_live/refs/heads/main/temp",
"https://raw.githubusercontent.com/develop202/migu_video/main/interface.txt",
"https://raw.githubusercontent.com/mzky/checklist/refs/heads/master/itvlist.m3u",
"https://raw.githubusercontent.com/qingtingjjjjjjj/iptv-auto-update/main/my.txt",
"https://raw.githubusercontent.com/Wirili/IPTV/main/live.txt",
"https://raw.githubusercontent.com/mymsnn/DailyIPTV/main/outputs/full_validated.m3u",
"https://raw.githubusercontent.com/fafa002/yf2025/refs/heads/main/yiyifafa.txt",
"https://raw.githubusercontent.com/nianxinmj/nxpz/refs/heads/main/lib/live.txt",
"https://raw.githubusercontent.com/yoursmile66/TVBox/main/live.txt",
"https://raw.githubusercontent.com/Guovin/iptv-api/gd/output/result.m3u",
"https://gongdian.top/tv/ku9/webview.txt#JS=https://gongdian.top/tv/ku9/js/webview.js",
"https://wget.la/https://github.com/Kimentanm/aptv/raw/master/m3u/iptv.m3u",
"https://tvv.tw/github.com/alantang1977/X/raw/main/live/live_ipv4.m3u",
    "http://103.236.75.89:588/psy.m3u",
    "http://4gtv.cnlive.club/4gtv.m3u",
    "https://4gtv.tvbjack.ggff.net",
    "http://4gtv.158.qzz.io/4gtv.m3u",
    "https://raw.githubusercontent.com/iodata999/frxz751113-IPTVzb1/refs/heads/main/结果.m3u",
    "https://raw.githubusercontent.com/alantang1977/jtv/refs/heads/main/网络收集.txt",
    "https://lytvs.top/py/custom_lives.m3u",
    "",
    "",
    "https://raw.githubusercontent.com/develop202/migu_video/main/interface.txt",
    "https://www.iyouhun.com/tv/myIPTV/ipv6.m3u",
    "https://www.iyouhun.com/tv/myIPTV/ipv4.m3u",
    "",   
    "https://live.izbds.com/tv/iptv4.txt",
    "https://l.gmbbk.com/upload/39183918.txt",
    "http://rihou.cc:555/gggg.nzk",
    "http://1.94.31.214/live/livelite.txt",
    "",
    "",
    "",
    "",
    "",
    "",
    "https://live.zbds.top/tv/iptv4.txt",
    "",


]

# 直播源黑名单URL列表，去除了重复项
url_blacklist = [
    "epg.pw/stream/",
    "103.40.13.71:12390",
    "[2409:8087:1a01:df::4077]/PLTV/",
    "http://[2409:8087:1a01:df::7005]:80/ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226419/index.m3u8",
    "http://[2409:8087:5e00:24::1e]:6060/000000001000/1000000006000233001/1.m3u8",
    "8.210.140.75:68",
    "154.12.50.54",
    "yinhe.live_hls.zte.com",
    "8.137.59.151",
    "[2409:8087:7000:20:1000::22]:6060",
    "histar.zapi.us.kg",
    "www.tfiplaytv.vip",
    "dp.sxtv.top",
    "111.230.30.193",
    "148.135.93.213:81",
    "live.goodiptv.club",
    "iptv.luas.edu.cn",
    "[2409:8087:2001:20:2800:0:df6e:eb22]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb23]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb1d]/ott.mobaibox.com/",
    "[2409:8087:2001:20:2800:0:df6e:eb1d]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb24]",
    "2409:8087:2001:20:2800:0:df6e:eb25]:80",
    "stream1.freetv.fun",
    "chinamobile",
    "gaoma",
    "[2409:8087:2001:20:2800:0:df6e:eb27]"
]

# 公告信息
announcements = [
    {
        "channel": "更新日期",
        "entries": [
            {
                "name": None,
                "url": "https://cnb.cool/junchao.tang/jtv/-/git/raw/main/Pictures/Robot.mp4",
                "logo": "https://cnb.cool/junchao.tang/jtv/-/git/raw/main/Pictures/Chao.png"
            }
        ]
    }
]

# EPG（电子节目指南）URL列表
epg_urls = [
    "https://epg.v1.mk/fy.xml",
    "http://epg.51zmt.top:8000/e.xml",
    "https://epg.pw/xmltv/epg_CN.xml",
    "https://epg.pw/xmltv/epg_HK.xml",
    "https://epg.pw/xmltv/epg_TW.xml"
]
# 测速超时时间（秒）
TEST_TIMEOUT = 3.5

# 测速线程池最大工作线程数
MAX_WORKERS = 10
# 单个频道单协议（IPv4/IPv6）最多保留的线路数量
MAX_CHANNEL_SOURCES = 3
# ── 质量检测 — HTTP 快筛 ─────────────────────────────────────────────
# enable_quality_check : True=启用质量检测（测活后过滤失效源），False=直接输出不过滤
# check_timeout        : 单个 URL HTTP 请求超时时间（秒），超时视为失效
# check_max_conn       : 最大并发检测数，调高可加速但更占带宽
enable_quality_check = True
check_timeout    = 3.5
check_max_conn   = 10

# ── 质量检测 — FFprobe 中度探测 ───────────────────────────────────────
# enable_ffprobe     : True=启用第二层 FFprobe 探测，False=仅 HTTP 快筛
#                      建议先在少量频道上测试稳定性，再全量开启
# ffmpeg_path        : FFprobe 可执行文件路径
#                      空字符串 = 使用系统 PATH 里的 ffprobe
#                      Windows 如不在 PATH 中，填绝对路径即可
# ffprobe_timeout    : 单个 URL FFprobe 探流超时（秒）
#                      IPTV 流通常 1~3 秒即可探完，设为 8 秒以容忍慢源
# min_bitrate        : 最低码率阈值（bps），低于此值且 ffprobe 能读到码率时被过滤
#                      设为 0 = 不限制码率（IPTV 流常读不到码率字段，此时代偿跳过检查）
# min_resolution     : 最低分辨率宽度要求（字符串，如 "720" 表示宽 >= 720px）
#                      设为空字符串 "" = 不限制分辨率
# ffprobe_max_streams: ffprobe 最多读取的流数量，避免大文件探流耗时过长
ffmpeg_path        = ""        # 空 = 使用系统 PATH 里的 ffprobe
enable_ffprobe     = True
ffprobe_timeout    = 3.5
min_bitrate        = 200000         # min_bitrate = 200000 → 码率>0 且 <200kbps 的源会被淘汰；码率=0 的源不受影响
min_resolution     = "1080"     # 宽度最低 1080px
ffprobe_max_streams = 3

# ── 深度探测配置 ───────────────────────────────────────────────────────
# enable_deep_probe  : True=启用第三层深度探测（仅对 m3u8 流），False=仅中度探测
#                      深度探测会检查分片时长、数量等，更准确但更慢
# deep_probe_timeout : 单个 URL 深度探测超时（秒）
#                      IPTV 流通常 5~10 秒即可探完，设为 10 秒以容忍慢源
# min_speed_kbps     : 最小速度阈值（kbps），低于此值的源会被过滤
#                      0 = 不过滤（只评分不淘汰）
#                      建议 2000（2 Mbps）避免推流卡顿
enable_deep_probe  = False
deep_probe_timeout = 5.0
min_speed_kbps     = 2500  # 2.5 Mbps
