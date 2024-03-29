import 'package:flutter/material.dart';
import 'package:libretv/domain/channel.dart';
import 'package:libretv/pages/scaffold.dart';
import 'package:media_kit/media_kit.dart';
import 'package:media_kit_video/media_kit_video.dart';

class ChannelPage extends StatefulWidget {
  static const String path = "/channel";
  final Channel channel;
  const ChannelPage({super.key, required this.channel});

  @override
  State<StatefulWidget> createState() => _ChannelPageState();
}

class _ChannelPageState extends State<ChannelPage> {
  late final Player player = Player();
  late final VideoController videoController = VideoController(player);
  late final Channel channel = widget.channel;
  int currentStream = 0;

  @override
  void initState() {
    player.open(Media(channel.streams[currentStream].url), play: false);
    super.initState();
  }

  @override
  void dispose() {
    player.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    double aspectRatio = 9.0 / 16.0;

    Size size = MediaQuery.of(context).size;
    Channel channel = widget.channel;
    return ScaffoldPage(
        body: Column(children: [
      SizedBox(
        width: size.width,
        height: size.width * aspectRatio,
        child: Video(controller: videoController),
      ),
      SizedBox(width: size.width, height: 20),
      Container(
          padding: const EdgeInsets.only(left: 20, right: 20),
          child: Column(
            children: [
              Align(alignment: Alignment.centerLeft, child: Text(channel.name)),
              Wrap(
                  spacing: 20,
                  alignment: WrapAlignment.start,
                  crossAxisAlignment: WrapCrossAlignment.start,
                  children: channel.streams
                      .asMap()
                      .entries
                      .map((entry) => GestureDetector(
                          onTap: () {
                            setState(() {
                              currentStream = entry.key;
                              player.open(Media(entry.value.url));
                            });
                          },
                          child: Container(
                              padding: const EdgeInsets.all(5),
                              decoration: BoxDecoration(
                                border: Border.all(),
                                color: entry.key == currentStream
                                    ? Colors.black
                                    : Colors.white,
                              ),
                              child: Text(
                                entry.value.quality,
                                style: TextStyle(
                                  color: entry.key == currentStream
                                      ? Colors.white
                                      : Colors.black,
                                ),
                              ))))
                      .toList())
            ],
          ))
    ]));
  }
}
