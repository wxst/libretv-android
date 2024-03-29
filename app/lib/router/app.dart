import 'package:go_router/go_router.dart';
import 'package:libretv/domain/channel.dart';
import 'package:libretv/pages/channel/page.dart';
import 'package:libretv/pages/home/page.dart';

final appRouter = GoRouter(initialLocation: HomePage.path, routes: [
  GoRoute(path: HomePage.path, builder: (context, state) => HomePage()),
  GoRoute(path: ChannelPage.path, builder: (context, state) => ChannelPage(channel: state.extra as Channel))
]);
