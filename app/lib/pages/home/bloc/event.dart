abstract class HomePageEvent {}

class HomePageFetch extends HomePageEvent {
  String search;
  HomePageFetch({required this.search});
}