//
//  Your Gallery.swift
//  HackingBirthdayBash-2
//
//  Created by Brayton Lordianto on 7/30/22.
//

import SwiftUI

struct Your_Gallery: View {
    private static let gridCount = 3
    @State private var gridColumns = Array(repeating: GridItem(.flexible()), count: gridCount)
    let images: [Image] = [
        Image(systemName: "person"),
        Image(systemName: "person.circle"),
        Image(systemName: "person"),
        Image(systemName: "person.circle"),
        Image(systemName: "person"),
        Image(systemName: "person"),
        Image(systemName: "person"),
        Image(systemName: "person")
    ]
    var body: some View {
        NavigationView {
            VStack {
                ScrollView {
                    LazyVGrid(columns: gridColumns) {
                        ForEach(images.indices, id: \.self) { index in
                            images[index]
                                .resizable()
                                .aspectRatio(1.0, contentMode: .fit)
                                .padding()
                        }
                    }
                }
            }
            .navigationTitle("Your Hackathon Journey")
        }
    }
}

struct Your_Gallery_Previews: PreviewProvider {
    static var previews: some View {
        Your_Gallery()
    }
}
