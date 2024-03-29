import 'package:libretv/domain/channel.dart';

abstract class HomePageState {}

class HomePageInitialState extends HomePageState {}

class HomePageLoadingState extends HomePageState {}

class HomePageLoadedState extends HomePageState {
  List<Channel> channels;
  HomePageLoadedState({required this.channels});
}

