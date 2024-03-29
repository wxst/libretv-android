import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:graphql_flutter/graphql_flutter.dart';
import 'package:libretv/app.dart';
import 'package:libretv/pages/home/bloc/bloc.dart';
import 'package:libretv/service_locator.dart';
import 'package:media_kit/media_kit.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  MediaKit.ensureInitialized();
  await serviceLocatorSetup();
  runApp(MultiBlocProvider(providers: [
    BlocProvider<HomePageBloc>(create: (context) => getIt.get<HomePageBloc>())
  ], child: App()));
}
