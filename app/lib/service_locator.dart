import 'package:get_it/get_it.dart';
import 'package:libretv/config/app_config.dart';
import 'package:libretv/config/app_config_impl.dart';
import 'package:libretv/pages/home/bloc/bloc.dart';

final getIt = GetIt.instance;

Future<void> serviceLocatorSetup() async {
  // Config
  getIt.registerSingleton<AppConfig>(AppConfigImpl());

  // Bloc
  getIt.registerSingleton<HomePageBloc>(HomePageBloc());
}
