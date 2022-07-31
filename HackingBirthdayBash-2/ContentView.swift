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
            Your_Gallery()
                .badge("new")
                .tabItem {
                    Label("Your Gallery", systemImage: "photo")
                }
            Form{
                TextField("\(Image(systemName: "magnifyingglass")) Search For Hacker Screen Names Here", text: .constant(""))
            }
                .tabItem {
                    Label("Create and Gift Badges", systemImage: "magnifyingglass.circle")
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
