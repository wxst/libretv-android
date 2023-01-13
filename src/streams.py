from m3u_parser import M3uParser
from constants import IPTV_STREAM_M3U
import pandas as pd
import os


streams = []


def load_streams():
    global streams
    # Parse m3u streams and save as csv at stream directory
    m3u = M3uParser()
    for path in os.listdir(IPTV_STREAM_M3U):
        stream = os.path.join(IPTV_STREAM_M3U, path)
        if os.path.isfile(stream) and stream.endswith(".m3u"):
            m3u.parse_m3u(stream, check_live=False)
            streams.append(pd.json_normalize(m3u.get_list(), sep="."))

    streams = pd.concat(streams)
