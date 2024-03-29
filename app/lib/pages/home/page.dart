import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:go_router/go_router.dart';
import 'package:libretv/pages/channel/page.dart';
import 'package:libretv/pages/home/bloc/bloc.dart';
import 'package:libretv/pages/home/bloc/event.dart';
import 'package:libretv/pages/home/bloc/state.dart';
import 'package:libretv/pages/scaffold.dart';
import 'package:libretv/service_locator.dart';

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
  TextEditingController search = TextEditingController();

  @override
  void initState() {
    widget.homePageBloc.add(HomePageFetch(search: search.text));
    super.initState();
  }

  @override
  void dispose() {
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;

    return ScaffoldPage(
        body: Column(
      children: [
        Container(
          padding: const EdgeInsets.only(left: 20, right: 20, top: 20),
          width: size.width,
          height: 40,
          child: const Text("LibreTV"),
        ),
        Container(
          padding: const EdgeInsets.only(left: 20, right: 20),
          width: size.width,
          height: 50,
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Expanded(child: TextField(controller: search)),
              const SizedBox(width: 20, height: 50),
              GestureDetector(
                onTap: () {
                  widget.homePageBloc.add(HomePageFetch(search: search.text));
                },
                child: const Align(
                    alignment: Alignment.bottomCenter,
                    child: Icon(Icons.search)),
              )
            ],
          ),
        ),
        SizedBox(width: size.width, height: 20),
        BlocBuilder<HomePageBloc, HomePageState>(
          builder: (BuildContext context, HomePageState state) {
            switch (state) {
              case HomePageLoadingState():
                return const Center(child: Text("Loading"));
              case HomePageLoadedState():
                return Expanded(
                  child: GridView.count(
                      crossAxisCount: 3,
                      children: state.channels
                          .map((channel) => Column(
                                children: [
                                  GestureDetector(
                                    onTap: () => {
                                      context.push(ChannelPage.path,
                                          extra: state.channels.firstWhere(
                                              (target) =>
                                                  target.id == channel.id))
                                    },
                                    child: Container(
                                        width: 80,
                                        height: 80,
                                        decoration: BoxDecoration(
                                            border: Border.all()),
                                        child: Image.network(channel.logo)),
                                  ),
                                  Text(channel.name),
                                ],
                              ))
                          .toList()),
                );
            }

            return const Center(child: Text("Initial State"));
          },
        ),
      ],
    ));
  }
}
