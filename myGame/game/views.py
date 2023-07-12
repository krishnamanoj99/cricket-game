from django.shortcuts import render, redirect


# Create your views here.
def store_data(request):
    if request.method == 'POST':
        name = request.POST.get('playerName')
        request.session['playerName'] = name

        player_team = request.POST.get('playerTeam')
        request.session['playerTeam'] = player_team

        oppo_team = request.POST.get('opponentTeam')
        request.session['opponentTeam'] = oppo_team

        if player_team == oppo_team:
            return render(request, 'game/index.html')
        else:
            return redirect('rules_view')
    else:
        return render(request, 'game/index.html')


def about_view(request):
    return render(request, 'game/about.html')


def rules_view(request):
    name = request.session.get('playerName')
    player_team = request.session.get('playerTeam')
    oppo_team = request.session.get('opponentTeam')

    context = {
        'player_name': name,
        'playerTeam': player_team,
        'oppoTeam': oppo_team
    }
    if request.method == 'POST':
        return redirect('toss_view')
    return render(request, 'game/rules.html', context)


def toss_view(request):
    name = request.session.get('playerName')
    player_team = request.session.get('playerTeam')
    oppo_team = request.session.get('opponentTeam')

    won_toss = request.GET.get('toss')
    bat_first = request.GET.get('bat_first')
    request.session['toss_winner'] = won_toss
    request.session['first_batting'] = bat_first

    context = {
        'player_name': name,
        'playerTeam': player_team,
        'oppoTeam': oppo_team,
        'toss_winner': won_toss,
        'first_batting': bat_first,
    }

    if bat_first == 'player':
        return render(request, 'game/player_batting_first.html', context)
    elif bat_first == 'computer':
        return render(request, 'game/player_bowling_first.html', context)

    return render(request, 'game/toss.html', context)


def batting_first_view(request):
    name = request.session.get('playerName')
    player_team = request.session.get('playerTeam')
    oppo_team = request.session.get('opponentTeam')
    won_toss = request.session.get('toss_winner')
    bat_first = request.session.get('first_batting')

    target = request.GET.get('target')
    first_innings_total = request.GET.get('first_innings')
    request.session['first_innings'] = first_innings_total

    context = {
        'player_name': name,
        'playerTeam': player_team,
        'oppoTeam': oppo_team,
        'toss_winner': won_toss,
        'first_batting': bat_first,
        'first_innings': first_innings_total,
        'target': target,
    }

    if int(target) >= 1:
        return render(request, 'game/player_bowling_second.html', context)

    return render(request, 'game/player_batting_first.html', context)


def bowling_first_view(request):
    name = request.session.get('playerName')
    player_team = request.session.get('playerTeam')
    oppo_team = request.session.get('opponentTeam')
    won_toss = request.session.get('toss_winner')
    bat_first = request.session.get('first_batting')

    target = request.GET.get('target')
    first_innings_total = request.GET.get('first_innings')
    request.session['first_innings'] = first_innings_total

    context = {
        'player_name': name,
        'playerTeam': player_team,
        'oppoTeam': oppo_team,
        'toss_winner': won_toss,
        'first_batting': bat_first,
        'first_innings': first_innings_total,
        'target': target,
    }

    if int(target) >= 1:
        return render(request, 'game/player_batting_second.html', context)

    return render(request, 'game/player_bowling_first.html', context)


def bowling_second_view(request):
    name = request.session.get('playerName')
    player_team = request.session.get('playerTeam')
    oppo_team = request.session.get('opponentTeam')
    won_toss = request.session.get('toss_winner')
    bat_first = request.session.get('first_batting')
    target = request.session.get('target')
    first_innings_total = request.session.get('first_innings')

    print(first_innings_total)

    result = None
    result = request.GET.get('result')
    second_innings_total = request.GET.get('second_innings')

    context = {
        'player_name': name,
        'playerTeam': player_team,
        'oppoTeam': oppo_team,
        'toss_winner': won_toss,
        'first_batting': bat_first,
        'target': target,
        'first_innings': first_innings_total,
        'second_innings': second_innings_total,
        'result': result
    }

    if result is not None:
        return render(request, 'game/result.html', context)

    return render(request, 'game/player_bowling_second.html', context)


def batting_second_view(request):
    name = request.session.get('playerName')
    player_team = request.session.get('playerTeam')
    oppo_team = request.session.get('opponentTeam')
    won_toss = request.session.get('toss_winner')
    bat_first = request.session.get('first_batting')
    target = request.session.get('target')
    first_innings_total = request.session.get('first_innings')

    result = request.GET.get('result')
    second_innings_total = request.GET.get('second_innings')

    context = {
        'player_name': name,
        'playerTeam': player_team,
        'oppoTeam': oppo_team,
        'toss_winner': won_toss,
        'first_batting': bat_first,
        'target': target,
        'result': result,
        'first_innings': first_innings_total,
        'second_innings': second_innings_total
    }

    if result is not None:
        return render(request, 'game/result.html', context)

    return render(request, 'game/player_batting_second.html', context)


def result_view(request):
    name = request.session.get('playerName')
    player_team = request.session.get('playerTeam')
    oppo_team = request.session.get('opponentTeam')
    won_toss = request.session.get('toss_winner')
    bat_first = request.session.get('first_batting')
    target = request.session.get('target')
    result = request.session.get('result')
    first_innings_total = request.session.get('first_innings')
    second_innings_total = request.session.get('second_innings')

    context = {
        'player_name': name,
        'playerTeam': player_team,
        'oppoTeam': oppo_team,
        'toss_winner': won_toss,
        'first_batting': bat_first,
        'target': target,
        'first_innings': first_innings_total,
        'second_innings': second_innings_total,
        'result': result
    }

    render(request, 'game/result.html', context)
