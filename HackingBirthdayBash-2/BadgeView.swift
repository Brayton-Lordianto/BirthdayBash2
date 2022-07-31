//
//  BadgeView.swift
//  HackingBirthdayBash-2
//
//  Created by Brayton Lordianto on 7/30/22.
//

import SwiftUI

struct BadgeView: View {
    var image: Image
    @State var print = false
    var body: some View {
            Form {
                Section {
                    VStack(alignment: .center) {
                        image
                            .padding()
                        Button("Print Now") {
                            print = true
                        }
//                        NavigationLink(destination: {
//                            Text("i")
//                        }, label: {Text("Print now")})
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
                    Text("June 20 2022")
                }
                
                Section("From Hackathon") {
                    Link("Microsoft Hackathon", destination: URL(string: "https://microsoft-did.devpost.com//")!)
                }
                
                Section("Issued By") {
                    Text("John Doe, Organizer")
                }
                
                Section("Personalized Message") {
                    Text("Thanks for your participation! Here's a token for you to remember. \n\nWe hope you join us again next time!")
                }
            }
            .navigationTitle("Hackathon Badge")
            .sheet(isPresented: $print) {
                PrinterPickerController(showPrinterPicker: $print)
            }
    }
}

struct BadgeView_Previews: PreviewProvider {
    static var previews: some View {
        BadgeView(image: Image("Badge1"))
    }
}
