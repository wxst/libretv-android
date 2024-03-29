import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:graphql_flutter/graphql_flutter.dart';
import 'package:libretv/domain/channel.dart';
import 'package:libretv/pages/home/bloc/event.dart';
import 'package:libretv/pages/home/bloc/state.dart';
import 'package:libretv/service_locator.dart';

class HomePageBloc extends Bloc<HomePageEvent, HomePageState> {
  late final GraphQLClient graphQLClient;
  HomePageBloc() : super(HomePageInitialState()) {
    graphQLClient = getIt.get<GraphQLClient>();
    on<HomePageFetch>(_onFetch);
  }

  _onFetch(HomePageEvent event, Emitter emit) async {
    if (event is HomePageFetch) {
      emit(HomePageLoadingState());
      final res = await graphQLClient.query(QueryOptions(document: gql("""
query {
  channels (length:100, stream:true, search:"${event.search}"){
    id
    logo
    name
    streams{
      resolution
      url
    }
  }
}
""")));

      List<Channel> channels = [];
      res.data?['channels']
          .forEach((channel) => channels.add(Channel.fromMap(channel)));
      emit(HomePageLoadedState(channels: channels));
    }
  }
}
