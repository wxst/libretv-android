import 'package:flutter/material.dart';
import 'package:libretv/config/app_config.dart';
import 'package:libretv/router/app.dart';
import 'package:libretv/service_locator.dart';

class App extends StatelessWidget {
  late final AppConfig appConfig;
  App({super.key}) {
    appConfig = getIt.get<AppConfig>();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(title: appConfig.name, routerConfig: appRouter);
  }
}
