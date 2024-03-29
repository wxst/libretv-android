import 'package:get_it/get_it.dart';
import 'package:graphql_flutter/graphql_flutter.dart';
import 'package:libretv/config/app_config.dart';
import 'package:libretv/config/app_config_impl.dart';
import 'package:libretv/pages/home/bloc/bloc.dart';

final getIt = GetIt.instance;

Future<void> serviceLocatorSetup() async {
  // Config
  getIt.registerSingleton<AppConfig>(AppConfigImpl());

  // storage
  await initHiveForFlutter();

  // GraphClient
  final HttpLink httpLink = HttpLink(
    'http://37.27.42.101:4011/',
  );
  GraphQLClient client = GraphQLClient(
    link: httpLink,
    // The default store is the InMemoryStore, which does NOT persist to disk
    cache: GraphQLCache(store: HiveStore()),
  );

  getIt.registerLazySingleton<GraphQLClient>(() => client);

  // Bloc
  getIt.registerSingleton<HomePageBloc>(HomePageBloc());
}
