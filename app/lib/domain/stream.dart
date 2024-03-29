import 'dart:convert';

class ChannelStream {
  final String url;

  ChannelStream({required this.url});

  factory ChannelStream.fromJson(String json) =>
      ChannelStream.fromMap(jsonDecode(json));

  String toJson() => jsonEncode(toMap());

  factory ChannelStream.fromMap(Map<String, dynamic> map) {
    return ChannelStream(url: map['url']);
  }

  Map<String, dynamic> toMap() {
    return {'url': url};
  }
}
