import 'dart:convert';

class ChannelStream {
  final String url;
  final String quality;

  ChannelStream({required this.url, required this.quality});

  factory ChannelStream.fromJson(String json) =>
      ChannelStream.fromMap(jsonDecode(json));

  String toJson() => jsonEncode(toMap());

  factory ChannelStream.fromMap(Map<String, dynamic> map) {
    return ChannelStream(url: map['url'], quality: map['resolution'] ?? "Standard");
  }

  Map<String, dynamic> toMap() {
    return {'url': url, 'resolution': quality};
  }
}
