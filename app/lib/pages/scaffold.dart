import 'package:flutter/material.dart';

class ScaffoldPage extends StatelessWidget {
  final Widget body;

  const ScaffoldPage({
    super.key,
    required this.body,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: SafeArea(
      top: true,
      bottom: true,
      left: true,
      right: true,
      child: body,
    ));
  }
}
