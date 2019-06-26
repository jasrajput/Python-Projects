def print_models(unprinted_design, completed_models):
    while unprinted_design:
        current_design = unprinted_design.pop()

        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(complete_models):
    print("\nThe following models have been printed")
    for complete_model in complete_models:
        print(complete_model)