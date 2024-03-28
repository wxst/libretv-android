import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:libretv/pages/home/bloc/bloc.dart';
import 'package:libretv/pages/home/bloc/event.dart';
import 'package:libretv/pages/home/bloc/state.dart';
import 'package:libretv/pages/scaffold.dart';
import 'package:libretv/service_locator.dart';
import 'package:media_kit/media_kit.dart';
import 'package:media_kit_video/media_kit_video.dart';

class HomePage extends StatefulWidget {
  static const String path = '/';
  late final HomePageBloc homePageBloc;
  HomePage({super.key}) {
    homePageBloc = getIt.get<HomePageBloc>();
  }

  @override
  State<StatefulWidget> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  late final Player player = Player();
  late final VideoController controller = VideoController(player);

  @override
  void initState() {
    widget.homePageBloc.add(HomePageFetch());
    super.initState();
  }

  @override
  void dispose() {
    player.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return ScaffoldPage(body: BlocBuilder<HomePageBloc, HomePageState>(
      builder: (BuildContext context, HomePageState state) {
        switch (state) {
          case HomePageInitialState():
            return const Center(child: Text("Initial State"));

          case HomePageLoadingState():
            return const Center(child: Text("Loading"));
        }

        Size size = MediaQuery.of(context).size;

        return Column(
          children: [
            SizedBox(width: size.width, height: 50, child: const Text("Search Bar"),),
            SizedBox(
                width: size.width,
                height: size.width * (9.0/16.0),
                child: Video(controller: controller)),
            TextButton(
                onPressed: () {
                  player.open(Media(
                      "http://stream.flynetwifi.com:1935/live/mobile-062/playlist.m3u8"));
                },
                child: const Text("Open"))
          ],
        );
      },
    ));
  }
}
