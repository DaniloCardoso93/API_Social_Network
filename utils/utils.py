def choices_error_message(choices_class):
    valid_choices = [choice[0] for choice in choices_class.choices]
    message = ", ".join(valid_choices).rsplit(",", 1)

    return "Choose between " + " and".join(message) + "."


def check_follows_or_friends(request, post_owner):
    for user in list(post_owner.followers.all()):
        if user.id == request.user.id:
            return True

    for friend in list(post_owner.receiving_friend.all()):
        if request.user.id == friend.sending_user_id:
            return friend.invitation == "Accepted"

    for friend in list(post_owner.sending_friend.all()):
        if request.user.id == friend.receiving_user_id:
            return friend.invitation == "Accepted"

    return False
