//
//  BadgeView2.swift
//  HackingBirthdayBash-2
//
//  Created by Brayton Lordianto on 7/31/22.
//

import SwiftUI

struct BadgeView2: View {
    var badge: Badge
    @State var print = false
    var body: some View {
            Form {
                Section {
                    VStack(alignment: .center) {
//                        Image(badge.imageURL.description)
                        AsyncImage(url: badge.imageURL) { image in
                            image
                                .resizable()
                                .scaledToFit()
                        } placeholder: {
                            ProgressView()
                        }
                            .padding()
                        Button("Print Now") {
                            print = true
                        }
                            .foregroundColor(.white)
                            .padding()
                            .background(.blue)
                            .cornerRadius(15)
                            .padding()
                    }
                    .frame(maxWidth: .infinity)
                }
                .background(.primary)
                .cornerRadius(20)
                
                Section("Date received") {
                    Text(badge.date)
                }
                
                Section("From Hackathon") {
                    Link(badge.hackathonLink.description, destination: badge.hackathonLink)
                }
                
                Section("Issued By") {
                    Text(badge.issuedBy)
                }
                
                Section("Personalized Message") {
//                    Text("Thanks for your participation! Here's a token for you to remember. \n\nWe hope you join us again next time!")
                    Text(badge.message)
                }
            }
            .navigationTitle("Hackathon Badge")
            .sheet(isPresented: $print) {
                PrinterPickerController(showPrinterPicker: $print)
            }
    }
}

struct BadgeView2_Previews: PreviewProvider {
    static var previews: some View {
        BadgeView2(badge: Badge(imageURL: URL(string: "https://images.credly.com/images/4ae74655-a8ba-4721-a075-e3ebcddd4657/hackathon_CHAMPION.png")!, date: "30 July 2022", hackathon: "some hacks", hackathonLink: URL(string: "https://www.google.com")!, issuedBy: "Hackathon Organizer", message: " some message "))
        
    }
}
