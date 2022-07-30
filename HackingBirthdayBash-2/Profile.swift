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
            VStack {
                Image(systemName: "person.crop.circle")
                    .resizable()
                    .frame(width: 100, height: 100)
                    .foregroundColor(.blue)
                Spacer()
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
