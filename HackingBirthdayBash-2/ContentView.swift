//
//  ContentView.swift
//  HackingBirthdayBash-2
//
//  Created by Brayton Lordianto on 7/30/22.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        TabView {
            Text("hi")
                .badge(2)
                .tabItem {
                    Label("Your Gallery", systemImage: "photo")
                }
            Text("f")
                .tabItem {
                    Label("Create and Gift Badges", systemImage: "tray.and.arrow.up.fill")
                }
            Profile()
                .badge("!")
                .tabItem {
                    Label("Profile", systemImage: "person.crop.circle.fill")
                }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
