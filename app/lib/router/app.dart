import 'package:go_router/go_router.dart';
import 'package:libretv/pages/home/page.dart';

final appRouter = GoRouter(initialLocation: HomePage.path, routes: [
  GoRoute(path: HomePage.path, builder: (context, state) => HomePage())
]);
