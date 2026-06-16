import 'package:flutter/material.dart';

import 'src/api/orca_api.dart';
import 'src/models.dart';
import 'src/screens/home_screen.dart';
import 'src/screens/login_screen.dart';

void main() {
  runApp(const OrcaMobileApp());
}

class OrcaMobileApp extends StatefulWidget {
  const OrcaMobileApp({super.key});

  @override
  State<OrcaMobileApp> createState() => _OrcaMobileAppState();
}

class _OrcaMobileAppState extends State<OrcaMobileApp> {
  final OrcaApi api = OrcaApi();
  AuthSession? session;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ORCA Mobile',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF7A4E25),
          primary: const Color(0xFF6E461F),
          secondary: const Color(0xFFD99C5F),
          surface: const Color(0xFFFFFBF6),
        ),
        scaffoldBackgroundColor: const Color(0xFFFAF7F1),
        appBarTheme: const AppBarTheme(
          backgroundColor: Color(0xFFFAF7F1),
          foregroundColor: Color(0xFF26170D),
          centerTitle: false,
        ),
        cardTheme: CardTheme(
          color: Colors.white,
          elevation: 0,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(14),
            side: const BorderSide(color: Color(0xFFE7DCCF)),
          ),
        ),
        inputDecorationTheme: InputDecorationTheme(
          filled: true,
          fillColor: Colors.white,
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(12),
            borderSide: const BorderSide(color: Color(0xFFE7DCCF)),
          ),
        ),
      ),
      home: session == null
          ? LoginScreen(
              api: api,
              onLoggedIn: (value) => setState(() => session = value),
            )
          : HomeScreen(
              api: api,
              session: session!,
              onLogout: () {
                api.logout();
                setState(() => session = null);
              },
            ),
    );
  }
}
