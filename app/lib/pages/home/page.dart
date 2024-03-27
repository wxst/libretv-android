import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:libretv/pages/home/bloc/bloc.dart';
import 'package:libretv/pages/home/bloc/event.dart';
import 'package:libretv/pages/home/bloc/state.dart';
import 'package:libretv/pages/scaffold.dart';
import 'package:libretv/service_locator.dart';

class HomePage extends StatefulWidget {
  static const String path = '/';
  late final HomePageBloc homePageBloc;
   HomePage({super.key}){
    homePageBloc = getIt.get<HomePageBloc>();
  }

  @override
  State<StatefulWidget> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  void initState() {
    widget.homePageBloc.add(HomePageFetch());
    super.initState();
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

        return const Center(child: Text("In Development"));
      },
    ));
  }
}
