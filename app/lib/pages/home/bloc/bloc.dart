import 'dart:async';

import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:libretv/pages/home/bloc/event.dart';
import 'package:libretv/pages/home/bloc/state.dart';

class HomePageBloc extends Bloc<HomePageEvent, HomePageState> {
  HomePageBloc() : super(HomePageInitialState()) {
    on<HomePageFetch>(_onFetch);
  }

  _onFetch(HomePageEvent event, Emitter emit) async {
    if (event is HomePageFetch) {
      emit(HomePageLoadingState());
      await Future.delayed(const Duration(seconds: 5));
      emit(HomePageLoadedState());
    }
  }
}
