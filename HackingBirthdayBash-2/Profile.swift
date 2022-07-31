//
//  Profile.swift
//  HackingBirthdayBash-2
//
//  Created by Brayton Lordianto on 7/30/22.
//

import SwiftUI

struct Profile: View {
    var body: some View {
        NavigationView {
            Form {
                Section {
                    VStack(alignment: .center) {
                        Image(systemName: "person.crop.circle")
                            .resizable()
                            .frame(width: 100, height: 100)
                            .foregroundColor(.blue)
                    }
                    .frame(maxWidth: .infinity)
                    .listRowBackground(Color.gray)
                }
                
                Section("Name") {
                    Text("Brayton Lordianto")
                }
                Section("devpost screen name") {
                    Text("bl3321")
                }
                Section("devpost link") {
                    Link("link", destination: URL(string: "https://devpost.com/bl3321")!)
                }
            }
            .navigationTitle("Profile")
        }
    }
}

struct Profile_Previews: PreviewProvider {
    static var previews: some View {
        Profile()
    }
}
