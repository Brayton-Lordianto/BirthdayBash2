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
        Image("Badge1"),
        Image("Badge2"),
        Image("Badge3"),
        Image("Badge4"),
        Image("Badge5")
    ]
    @ObservedObject var gallery: Gallery = Gallery()
    var body: some View {
        NavigationView {
            VStack {
                Text("Click on a badge to learn more!")
                    .foregroundColor(.gray)
                    .italic()
                
                if true {
                    ScrollView {
                        LazyVGrid(columns: gridColumns) {
                            ForEach(gallery.badges.indices, id: \.self) { index in
                                NavigationLink {
                                    //                                BadgeView(image: images[index])
                                    BadgeView2(badge: gallery.badges[index])
//                                    Text("")
                                } label: {
//                                    images[index]
                                    AsyncImage(url: gallery.badges[index].imageURL) { image in
                                        image
                                            .resizable()
                                            .scaledToFit()
                                    } placeholder: {
                                        ProgressView()
                                    }
//                                    .resizable()
                                    .aspectRatio(1.0, contentMode: .fit)
                                    .padding()
                                }


                            }
                        }
                    }
                    Link("View Your Badges On Our Website Instead!", destination: URL(string: "https://hacker-hall-of-fame.typedream.app/")!)
                        .padding()
                }
            }
            .navigationTitle("My Hackathon Journey")
        }
    }
}

struct Your_Gallery_Previews: PreviewProvider {
    static var previews: some View {
        Your_Gallery()
    }
}
