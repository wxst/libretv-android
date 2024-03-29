import 'dart:convert';

import 'package:libretv/domain/stream.dart';

class Channel {
  final String id;
  final String name;
  final String logo;
  final List<ChannelStream> streams;

  Channel(
      {required this.id,
      required this.name,
      required this.logo,
      required this.streams});

  factory Channel.fromJson(String json) => Channel.fromMap(jsonDecode(json));

  String toJson() => jsonEncode(toMap());

  factory Channel.fromMap(Map<String, dynamic> map) {

    final List<ChannelStream> streams = [];
    map["streams"].forEach((stream) => streams.add(ChannelStream.fromMap(stream)));

    return Channel(
      id: map['id'],
      name: map["name"],
      logo: map["logo"],
      streams: streams
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'name': name,
      'logo': logo,
      'streams': jsonEncode(streams.map((stream) => stream.toJson()).toList())
    };
  }
}
